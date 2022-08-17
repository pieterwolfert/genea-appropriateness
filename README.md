# genea-appropriateness
Scripts to run Barnard's test on JSON output from the appropriateness study of GENEA 2022.

Steps to reproduce GENEA 2022 results:
- run app_analysis.py with the corresponding JSON output from the HEMVIP system
- run app_analysis_multi.py with the CSV file from the first script as input. This will calculate Barnard's test. This takes a while to process. 

If you use this material, please cite our latest paper on the GENEA Challenge 2022. At the time of writing (2022-08-08) this is our ACM ICMI 2022 paper:

Youngwoo Yoon, Pieter Wolfert, Taras Kucherenko, Carla Viegas, Teodor Nikolov, Mihail Tsakov, and Gustav Eje Henter. 2022. The GENEA Challenge 2022: A large evaluation of data-driven co-speech gesture generation. In Proceedings of the ACM International Conference on Multimodal Interaction (ICMI '22). ACM.

You can find the latest information and a BibTeX file on the project website:

https://youngwoo-yoon.github.io/GENEAchallenge2022/
