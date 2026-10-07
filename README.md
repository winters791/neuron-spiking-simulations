# Neuron Spiking Simulator

A software simulation of spiking neural networks running on simulated memristive crossbar hardware, where the same devices both store synaptic weights and compute with them.

Neurons follow Izhikevich's *Simple Model of Spiking Neurons* (2003). Synapses are modelled as an analog in-memory computing crossbar, following Sebastian et al., *Memory devices and applications for in-memory computing* (2020): weights are stored as device conductances, and the multiply-accumulate happens through Ohm's and Kirchhoff's laws.

## Status

Work in progress.

- [x] Single Izhikevich neuron (regular spiking)
- [ ] Firing-pattern presets (RS, IB, CH, FS, LTS, TC, RZ)
- [ ] 1000-neuron network with spike raster
- [ ] Crossbar synapses with device non-idealities (quantization, noise, drift, ADC precision)
- [ ] Interactive dashboard
- [ ] Associative memory demo
- [ ] STDP learning in place

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python nueron1.py
```

## References

- E. M. Izhikevich, "Simple Model of Spiking Neurons," *IEEE Transactions on Neural Networks*, 14(6), 2003.
- A. Sebastian, M. Le Gallo, R. Khaddam-Aljameh, E. Eleftheriou, "Memory devices and applications for in-memory computing," *Nature Nanotechnology*, 15, 2020.
