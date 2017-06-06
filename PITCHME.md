### ReBBR: Reproducing BBR Performance on Lossy Networks


<br>
<br>
<br>

<small>Luke Hsiao and Jervis Muindi</small>

June 2017

---

#### Introduction: BBR Congestion-based Congestion Control

* Tries to maximize throughput and minimize latency
* Does so by estimating the bottleneck bandwidth and round-trip propagation
  delay

---?image=http://deliveryimages.acm.org/10.1145/3030000/3022184/vanjacobson1.png


---

#### Sub-Result: BBR performs better than CUBIC in Lossy Networks
* We focus on the claim that BBR is better than CUBIC in networks with
  non-negligible loss rates.
* Illustrates one of the most obvious differences between a loss-based
  congestion control algorithm and a congestion-based algorithm.

---

![Fig8](http://deliveryimages.acm.org/10.1145/3030000/3022184/vanjacobson8.png)

BBR vs. CUBIC throughput for 60-second flows on a 100Mbps/100-ms link with
0.001% to 50% random loss.

---

#### Experimental Setup
- Ubuntu 16.04 LTS upgraded with [v4.11.1](http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.11.1/) of the Linux kernel
- [Mahimahi](http://mahimahi.mit.edu/) Network Emulator
- Google Cloud `n1-standard-2` instance
- Infinite buffer on bottleneck link
- 6.25MB maximum send and receive window sizes

---
