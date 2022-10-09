#%% Imports
from __future__ import annotations

#%% Read file, Parse YAML front matter
from pathlib import Path
f = Path('plan.md')
text = f.read_text()

import yaml
*rst, yaml_text, md = text.split('---')
yaml_text = yaml_text.strip()
yaml_text


plan: Plan = yaml.load(yaml_text, Loader=yaml.CSafeLoader)
plan

#%% Get Files
from collections import defaultdict

files = {}

for session in plan['sessions']:
    for unit in session['units']:
        if 'file' in unit:
            file = unit['file']
            path = Path(file)
            assert path.exists(), f"File {path.resolve()} does not exist"
            workshop_path = Path() / session['foldername'] / unit['filename']
            files[workshop_path] = path
     



files

# %% Clear Workshop Folder
from shutil import rmtree
basedir = Path('workshop')
rmtree(basedir, ignore_errors=True)


# %% Create Workshop Folder
from shutil import copy2


basedir = Path('workshop')
for to_path, from_path in files.items():
    full_path = basedir / to_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    copy2(from_path, full_path)



# %% Make Readme

from datetime import time, timedelta, datetime

readme_lines = []

readme_lines.append('#' * nested.level + f" {plan['title']}")


for session in plan['sessions']:
    

    # Track time
    schedule = session['schedule']
    breaks = schedule['breaks'].copy()
    current_time = datetime.strptime(schedule['startTime'], "%H:%M")

    # Day Title
    readme_lines.append(f"## {session['title']}: {schedule['startTime']}-{schedule['endTime']}")
    
    for unit in session['units']:
        total_mins = unit['minutes']
        duration = timedelta(minutes=total_mins)
        start, end = current_time, current_time + duration
        current_time = end
        # line = f"  - **({start.strftime('%H:%M')} - {end.strftime('%H:%M')}) {unit['title']} ({total_mins} mins)**"
        line = f"  - **{unit['title']}**"
        if 'filename' in unit:
            line += f": [Notebook]({unit['filename']})"
        readme_lines.append(line)
        # Check for Break
        if breaks and current_time > datetime.strptime(breaks[0]['doAfter'], "%H:%M"):
            curr_break = breaks[0]
            breaks: list
            breaks.remove(curr_break)
            start = datetime.strptime(curr_break['doAfter'], "%H:%M")
            end = start + timedelta(minutes=curr_break['minutes'])
            if curr_break['fixed']:
                line = f"  - **({start.strftime('%H:%M')} - {end.strftime('%H:%M')}) {curr_break['title']} **"
            else:
                line = f"  - {curr_break['title']}"
            readme_lines.append(line)



readme_text = '\n'.join(readme_lines)
print(readme_text)
(workshop / "README.md").write_text(readme_text)

