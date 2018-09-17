# ox-dictionary
A Python wrapper for the oxforddictionary.com REST API.

# Installation:
```shell
    download the wrapper.py file and executor.py(optional)
```

# Setup:
Require the wrapper module then create an OxfordD object using your url, app_id, app_key and language
```python
  o = OxfordD('url','<app_id>','<app_key>','<language>')
```

# Supported Methods:
Methods which are supported in this wrapper are as follows, more will be added in the future.

## .get_definition
`.get_definition` retrieves the definition for any given word as long as it can be found in the oxford dictionary.
```python
  o.get_definition("word")
```
## .get_example
`.get_example` retrieves an example sentence for a given word to provide insight on its usage
```python
  o.get_example("word")
```
## .get_pronunciation
`.get_pronunciation()` retrieves pronunciations for a given word in the phonetic spelling
```python
  o.get_pronunciation("word")
```
## .get_random_word
`.get_random_word()` provides any random word from the wordslist in the api, no parameter needs to be passed 
```python
  o.get_random_word()
```
## .get_synonym
`.get_synonym()` retrieves synonyms for a given word
```python
  o.get_synonym("word")
```
## .get_antonym
`.get_antonym`retrieves antonyms for a given word
```python
 
  o.get_antonym("word")
```
