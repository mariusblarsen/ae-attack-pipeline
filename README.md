# Pipeline for adversarial input attacks against obstacle detection
Repository for the Specialization project at NTNU fall 2021.

**Authors**
- [Johannes Åsheim](https://github.com/johanaas)
- [Kim Midtlid](https://github.com/kamidtli)
- [Marius Bæver Larsen](https://github.com/mariusblarsen)

# Todo
- [ ] Possibility to change/add models
- [ ] Possibility to change/add attacks
- [ ] Option for GPU acceleration (When training is needed)
- [ ] Add defence step

# Setup
**1.** Create and activate new environment
```Shell
python -m venv project
```

Linux:
```Shell
source project/Scripts/activate
```
Windows:
```Shell
.\project\Scripts\activate 
```
**2.** Install ipykernel and add virtual environment to the Python Kernel
```Shell
pip install ipykernel
```
```Shell
python -m ipykernel install --user --name=project
```
