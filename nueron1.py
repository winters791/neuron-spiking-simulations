import matplotlib.pyplot as plt

HALF_DT = 0.5   # ms; v is advanced in two half-steps per 1 ms step
V_PEAK = 30.0   # mV; spike cutoff where we reset

class Neuron:
    def __init__(self, a, b, c, d, v0=-65.0):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.v = v0
        self.u = b * v0

def step(n, I):
    """Advance neuron n by 1 ms with input I. Return True if it spiked."""
    for _ in range(2):
        n.v += HALF_DT * (0.04 * n.v**2 + 5 * n.v + 140 - n.u + I)
    n.u += n.a * (n.b * n.v - n.u)
    if n.v >= V_PEAK:
        n.v = n.c
        n.u += n.d
        return True
    return False

def simulate(n, I, T):
    """Run n for T ms with constant input I. Return v trace, u trace, spike times (ms)."""
    v_trace, u_trace, spike_times = [], [], []
    for t in range(T):
        if step(n, I):
            v_trace.append(V_PEAK)
            spike_times.append(t)
        else:
            v_trace.append(n.v)
        u_trace.append(n.u)
    return v_trace, u_trace, spike_times

if __name__ == "__main__":
    T = 1000
    n = Neuron(a=0.02, b=0.2, c=-65, d=8)
    v_trace, u_trace, spikes = simulate(n, I=10, T=T)
    print(f"{len(spikes)} spikes in {T} ms")

    fig, (ax_v, ax_u) = plt.subplots(2, 1, sharex=True, figsize=(8, 5))
    ax_v.plot(v_trace)
    ax_v.set_ylabel("v (mV)")
    ax_v.set_title("Regular-spiking neuron, I = 10")
    ax_u.plot(u_trace, color="tab:orange")
    ax_u.set_ylabel("u (recovery)")
    ax_u.set_xlabel("time (ms)")
    plt.tight_layout()
    plt.show()
