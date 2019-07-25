- Copy Template/ folder into a new cur_disease folder:
```
cp -r Template [cur_disease]
```


- Replace `_DISEASE_NAME_` with current disease's name:
```
find . -type f -exec sed -i 's/_DISEASE_NAME_/[cur_disease]/g' {} +
```
