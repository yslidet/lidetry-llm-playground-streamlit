# [LiDETry] Multimodel LLM Playgrounds 
Using streamlit as a platform to deploy LLM models. It acts as playground to test input prompt to the model. 

### Project Structure 
This project directory is as followed: 
```
    .
    ├── app                               
    │   ├── init.py                         <- empty; making 'app' a python package
    │   ├── main.py                         <- Streamlit control (set platform style, run app)
    │   ├── model.py                        <- model; generate output
    |   ├── my_key.py                       * create your own (follow "usage" instruction)
    │   ├── ui.py                           <- platform view/UI
    │   └── utils.py                        <- util (regex functions, ...)
    ├── run.py                              <- main execution file
    └── README.md
```


## Usage
* Install Dependencies `conda env create -f environment_llm-mac-intel.yaml`
* Add API_KEY to `mykey.py` at `app/mykey.py`
    * Setup OpenAI API key [(if you do not have)](https://platform.openai.com/api-keys); reference: [documentation](https://platform.openai.com/docs/quickstart?language-preference=python&quickstart-example=completions&desktop-os=macOS)
```python
API_KEY = "[your openai api key]"
```
* Start: `bash run.sh` or
```bash
streamlit run run.py --server.port=8050 --server.address=0.0.0.0 
```
* Stop `Ctl+C` (at the terminal)

## Acknowledgement
> **[LiDETry]** series is centered on exploring projects of interest as I believe that the best way to learn is by "DOing". 
-- While I might make minor adjustments, I would like to acknowledge and give credit the original tutorial(s)/project(s) referenced here. 

Note: modified from the original where BASE_URL is `https://api.openai.com/v1` instead of `https://integrate.api.nvidia.com/v1`

* https://medium.com/@subhraj07/building-a-dynamic-multi-model-llm-playground-a-comparative-journey-with-gemma2-nvidia-nemotron-7e3d8b9a998d
* https://github.com/subhrajit-mohanty/medium-blogs/tree/master/llm-playground-app
