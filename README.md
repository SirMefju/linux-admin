## linux-admin

## List of crazy commands which I use sometimes
* [Count line of code in files with same extension in location](#Count-line-of-code-in-files-with-same-extension-in-location)

### Count line of code in files with same extension in location
```R
find [location] -name '*'.py -exec cat {} \; | wc -l;
```
