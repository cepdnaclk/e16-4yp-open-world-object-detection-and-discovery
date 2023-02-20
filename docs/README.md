---
layout: home
permalink: index.html
# Please update this with your repository name and title
repository-name: e16-4yp-open-world-object-detection-and-discovery
title: Open World Object Detection and Discovery
---

# Open World Object Detection and Discovery

#### Team

- E/16/078, Thilini Deshika, [email](mailto:e16078@eng.pdn.ac.lk), [GitHub](https://github.com/Thilini-Deshika)
- E/16/168, Sudam Kalpage, [email](mailto:e16168@eng.pdn.ac.lk), [GitHub](https://github.com/sudamkalpage)
- E/16/369, Rusiru Thushara, [email](mailto:e16369@eng.pdn.ac.lk), [GitHub](https://github.com/thusharakart)

#### Supervisors

- Prof. Roshan G. Ragel, [email](mailto:roshanr@eng.pdn.ac.lk)
- Prof. Salman Khan, [email](mailto:salman.khan@mbzuai.ac.ae)
- Mr. Gihan Chanka Jayatilaka [email](mailto:gihan@umd.edu)

#### Project Summary
Object detection is a well-known computer vision technique for locating instances of objects in images. Open World Object Detection refers to tackling object detection tasks in an open-world setting where the task is to detect a known set of object categories while simultaneously identifying unknown objects. Moreover, it is required to identify instances of unknown objects and subsequently learns to recognize them when training data progressively arrive. An oracle (eg: - a human annotator) is needed to introduce new class labels for the identified unknowns to classify those to relevant object classes in the next increments of learning steps. The task was first introduced with Open World Object Detector (ORE), which classifies unknown objects into a single class named 'unknown'. Additionally, ORE incrementally learns new classes that become known in the next training episodes without forgetting previously learned classes. The recent paper OW-DETR introduces a multi-scale context-aware detection framework based on vision transformers to effectively detect unknown objects in the open-world setting. 

The Novel Class Discovery (NCD) is an image recognition problem, where novel classes are classified under the open-world setting. Generalized Category Discovery (GCD) proposes the use of vision transformers with contrastive representation learning to generalize the NCD problem. Here, unlabelled images can belong to either known or novel classes. These unlabelled images are categorized into two categories; 'seen' or 'unseen', using an effective semi-supervised k-means clustering approach. However, the existing detection methods do not tackle open-world detection under the GCD setting. To fill this gap, we proposed an unknown clustering mechanism for OW-DETR by merging the GCD setting with open-world object detection. After identifying the unknown objects as ‘unknown’, they are further clustered into several categories with the use of an unsupervised clustering mechanism. When new class labels are introduced, the model incrementally learns them without forgetting the previously learned classes. 

Key contributions:
- A Vision transformer-based deep learning model for object detection in open-world settings.
- An unsupervised clustering mechanism and a semisupervised clustering mechanism for categorizing detected unknown objects.
- Demonstration of a real-world application by performing the traffic sign detection task comes under autonomous driving.


<!--
#### Table of content

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
5. [Results and Analysis](#results-and-analysis)
6. [Conclusion](#conclusion)
7. [Publications](#publications)
8. [Links](#links)

---

## Abstract

## Related works

## Methodology

## Experiment Setup and Implementation

## Results and Analysis

## Conclusion

## Publications
-->
<!-- 1. [Semester 7 report](./) -->
<!-- 2. [Semester 7 slides](./) -->
<!-- 3. [Semester 8 report](./) -->
<!-- 4. [Semester 8 slides](./) -->
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->


## Links

- [Project Repository](https://github.com/cepdnaclk/e16-4yp-open-world-object-detection-and-discovery/)
- [Project Page](http://cepdnaclk.github.io/e16-4yp-open-world-object-detection-and-discovery/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [Faculty of Engineering](http://www.eng.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

