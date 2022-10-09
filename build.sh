conda activate py10
python utils/get_requirements.py notebooks/*.ipynb \
    | sort \
    | uniq \
    | grep -vxF BioPython \
    > requirements.txt

echo jupyterlab >> requirements.txt
echo jupyterlab-git >> requirements.txt
echo jupyterlab-link-share >> requirements.txt
echo pytest >> requirements.txt