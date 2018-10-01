import yaml

with open('config.json', 'r') as f:
    loaded = yaml.load(f.read())
    locals().update(loaded)
