import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc


# message OrderMessage {
#  enum Status {
#    QUEUED = 0;
#    PROCESSING = 1;
#    COMPLETED = 2;
#    FAILED = 3;
#  }

#  enum Equipment {
#    KEYBOARD = 0;
#    MOUSE = 1;
#    WEBCAM = 2;
#    MONITOR = 3;
#  }

#  string id = 1;
#  string created_by = 2;
#  Status status = 3;
#  string created_at = 4;
#  repeate

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def Create(self, request, context):
        print("Create new order")
        request_value = {
            "id": int(request.id),
            "created_by": request.created_by,
            "created_at": request.created_at,

            "Equipment": request.equipment,
            "Status": request.status

        }
        print(request_value)
        return order_pb2.orderMessage(**request_value)

    def Get(self, request, context):
        print("Orderslist has been requeted")

        # hard coded orders

        order1 = order_pb2.OrderMessage(
            id="123",
            created_by="Khalil",
            created_at="3010202216:30",
            equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD],
            status=order_pb2.OrderMessage.Status.PROCESSING
        )

        order2 = order_pb2.OrderMessage(
            id="456",
            created_by="Khalil",
            created_at="3010202216:40",
            equipment=[order_pb2.OrderMessage.Equipment.MONITOR],
            status=order_pb2.OrderMessage.Status.QUEUED
        )

        result = order_pb2.OrderMessageList()
        result.orders.extend([order1, order2])
        return result



# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
