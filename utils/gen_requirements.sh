python utils/get_requirements.py topics/**/*.ipynb \
    | sort \
    | uniq \
    | grep -vxF BioPython \
    > requirements.txt

echo "pytest" >> requirements.txt
echo "jupyerlab" >> requirements.txt
echo "jupyterlab-link-share" >> requirements.txt
echo "jupyterlab-git" >> requirements.txt