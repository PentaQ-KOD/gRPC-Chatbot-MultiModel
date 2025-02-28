import grpc
from concurrent import futures
import llm_service_pb2
import llm_service_pb2_grpc
import google.protobuf.struct_pb2 as struct_pb2
from models.gemini_model import GeminiAPI
from models.deepseek_model import DeepSeekAPI
from models.Llama_model import LlamaModelAPI


class LLMService(llm_service_pb2_grpc.LLMServiceServicer):
    def __init__(self):
        self.agents = {
            "Gemini": GeminiAPI(),
            "Deepseek": DeepSeekAPI(),
            "Llama": LlamaModelAPI(),
        }

    def Handshake(self, request, context):
        response = struct_pb2.Struct()
        response.update({"status": "Handshake successful"})
        return llm_service_pb2.HandshakeResponse(json_config=response)

    def GenerateText(self, request, context):
        response = struct_pb2.Struct()
        agent = self.agents.get(request.agent_name)

        if request.agent_name == "None":
            response.update({"response": request.input})
        elif agent:
            response.update({"response": agent.generate_text(request.input)})
        else:
            response.update({"error": "Unknown agent"})

        return llm_service_pb2.TextResponse(json_config=response)

    def StreamText(self, request, context):
        agent = self.agents.get(request.agent_name)

        if request.agent_name == "None":
            yield llm_service_pb2.TextResponse(
                json_config=struct_pb2.Struct(
                    fields={"response": struct_pb2.Value(string_value=request.input)}
                )
            )
        elif agent:
            for chunk in agent.stream_text(request.input):
                yield llm_service_pb2.TextResponse(
                    json_config=struct_pb2.Struct(
                        fields={"response": struct_pb2.Value(string_value=chunk)}
                    )
                )
        else:
            yield llm_service_pb2.TextResponse(
                json_config=struct_pb2.Struct(
                    fields={"error": struct_pb2.Value(string_value="Unknown agent")}
                )
            )

    def DeleteAgent(self, request, context):
        response = struct_pb2.Struct()
        response.update({"status": f"Agent {request.agent_name} deleted"})
        return llm_service_pb2.DeleteAgentResponse(json_config=response)


# Start gRPC Server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    llm_service_pb2_grpc.add_LLMServiceServicer_to_server(LLMService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("🚀 gRPC Server started at port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
