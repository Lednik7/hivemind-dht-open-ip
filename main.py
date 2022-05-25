import hivemind

dht = hivemind.DHT(
    host_maddrs=["/ip4/0.0.0.0/tcp/0", "/ip4/0.0.0.0/udp/0/quic",
                 "/ip6/0.0.0.0/tcp/0", "/ip6/0.0.0.0/udp/0/quic"],
    start=True)

print('\n'.join(str(addr) for addr in dht.get_visible_maddrs()))
print("Global IP:", hivemind.utils.networking.choose_ip_address(dht.get_visible_maddrs()))

input()