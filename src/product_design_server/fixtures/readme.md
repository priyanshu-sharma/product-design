### Loading fixtures

Whenever you modify any content of the fixtures/ directory, you need to run
```python
python manage.py loaddata fixtures/*.yaml
```
or in case of a specific file, let's say `001_product.yaml`
```python
python manage.py loaddata fixtures/001_product.yaml
```

This can be done by `ssh`ing into an EC2 box or by `exec` into a k8s pod.