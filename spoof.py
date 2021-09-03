import netfilterqueue

# Create an instance of netfilterqueue
queue = netfilterqueue.NetfilterQueue()

def process_packet(packet):
    print(packet)
    # Forward Packets
    # packet.accept()
    # Intercept and Drop Packets
    packet.drop()

queue.bind(0, process_packet)
queue.run()
