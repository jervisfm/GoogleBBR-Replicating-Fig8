## ReBBR: Reproducing BBR Performance on Lossy Networks

Luke Hsiao and Jervis Muindi

June 2017

---

### Introduction: BBR Congestion-based Congestion Control

* Tries to maximize throughput and minimize latency
* Does so by estimating the bottleneck bandwidth and round-trip propagation
  delay

---?image=http://deliveryimages.acm.org/10.1145/3030000/3022184/vanjacobson1.png


---

### Sub-Result: BBR performs better than CUBIC in Lossy Networks
* We focus on the claim that BBR is better than CUBIC in Lossy Networks
* Illustrates one of the most obvious differences between a loss-based
  congestion control algorithm and a congestion-based algorithm.

---
BBR vs CUBIC on a 100Mbps/100-ms link.
![Fig8](http://deliveryimages.acm.org/10.1145/3030000/3022184/vanjacobson8.png)
