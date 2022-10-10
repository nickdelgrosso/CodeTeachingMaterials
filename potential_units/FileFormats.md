
#  Structuring Data on Disk: Working with Files and File Formats in Python

## Text Formats

Open formats have open *specifications* that tools can reference in order to ensure compatibility.  This does not guarantee that tools will conform to them, but does help; as formats become popular across tools, there comes a natural pressure for these tools to fit these standards in order to be feature-complete.  Some examples:

  - **JSON**: https://www.json.org/json-en.html
  - **CSV**: https://tools.ietf.org/html/rfc4180 
  - **XML**: https://www.w3.org/TR/xml/
  - **YAML**: https://yaml.org/spec/1.2/spec.html
  - **ICAL**: https://tools.ietf.org/html/rfc5545

### Example: JSON in Python

#### Writing

```python
from pathlib import Path
import json

data = {"a": 3, "b": 4}
json_string = json.dumps(data)  # "Dump structure to json string"
Path("mydata.json").write_text(json_string)
```

#### Reading

```python
from pathlib import Path
import json

json_string = Path("mdata.json").read_text()
data = json.loads(json_string)  # Load string from json string
```

## Binary Formats

Binary data is the same, with way more examples depending on the type of data being stored.  Some are domain-specific (e.g. Image Formats: JPG, PNG, TIFF, etc), others are platform-specific (e.g. language: MAT, PKL), and others are more general (e.g. H5).  

Binary formats rely on software to be useful; they tend to be much more complex than text formats.  Tools conform to them via open specifications and validation software that checks that what they create works.  

### Examples

#### Pickle

```python
from pathlib import Path
import pickle

data1 = {"a": 3, "b": 4}
data2 = {"c": 3, "d": 4}
file = Path("mydata.json").open("wb")
pickle.dump(data1, file)  # "Dump structure to pickle.
pickle.dump(data2, file)  # "Dump structure to pickle.
file.close()
```

```python
from pathlib import Path
import pickle

file = Path("mydata.json").open("rb")
data1 = pickle.load(file)  # {"a": 3, "b": 4}
data2 = pickle.load(file)  # {"c": 3, "d": 4}
file.close()
```

#### MAT

```python
from scipy.io import loadmat, savemat

data1 = {"a": 3, "b": 4}
savemat("myfile.mat", data1)
data2 = loadmat("myfile.mat")
```

#### Images

```python
from matplotlib.pyplot import imread, imsave

image_array = plt.imread("bird.jpg")
plt.imsave("bird2.png", image_array)
```

#### HDF5

```python
import h5py

data = [3, 4, 5]
file = h5py.File("myfile.h5", "w")
file.create_dataset("numbers", data)
file.close()
```

## File Processing Exercise: Bird Image Database 

  1. **Raw Data Creation**:   The file *species.txt* contains a list of bird species, one on each line.  Manually make a new file in the same folder, *urls.txt*, containing a matching list of web urls to an image of each species (e.g. http://birdfans.com/robin.jpg)

  2. **Processed Data Creation**:  Write a script *image_download.py* that opens these two files and loops through the lines, downloading each image Fill the processed data folder with images with file names matching the bird species and an extension matching the url's extension.  (e.g. robin.jpg)

  Download Files with the *requests* package:

  ```bash
  python -m pip install requests
  ```

  ```python
  import requests
  response = requests.get("https://www.google.com")
  response.status_code  # should be 200 if successful
  data = response.contents  # for an image, this will be the raw image data, as a byte string.
  ```


  3. **Final Data Creation**: Each of these files are still a bit raw (different formats, for example).  Write a script *process_data.py* that loads each of these images into arrays and puts them together into a single file. (e.g. "birds.pkl" "birds.h5", "birds.mat")





