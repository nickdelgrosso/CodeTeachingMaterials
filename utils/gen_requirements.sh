python utils/get_requirements.py topics/**/*.ipynb \
    | sort \
    | uniq \
    | grep -vxF BioPython \
    > requirements.txt

echo "pytest" >> requirements.txt