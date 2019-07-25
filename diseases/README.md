- Copy Template/ folder into a new cur_disease folder:
```
cp -r Template [cur_disease]
```


- Replace `Epilepsy` with current disease's name:
```
find . -type f -exec sed -i 's/Epilepsy/[cur_disease]/g' {} +
```
