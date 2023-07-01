N, W, H, L = map(int, input().split())

can_w = W // L
can_h = H // L

print(min(N, can_w * can_h))
