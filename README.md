### Interesting scripts used to manage resources
* [Count lines of code in files with the same extensions](https://github.com/SirMefju/linux-admin/blob/main/scripts/extensions_with_loc.py)

### List of crazy commands which I use sometimes
* [Count line of code in files with same extension in location](#Count-line-of-code-in-files-with-same-extension-in-location)
* [Show which extensions are in location](#Show-which-extensions-are-in-location)
* [Count line of code in files with same extension in location typed in file](#Count-line-of-code-in-files-with-same-extension-in-location-typed-in-file)
* [Show life changes in txt file](#Show-life-changes-in-txt-file)

#### Count line of code in files with same extension in location
```cmd
find [location] -name '*'.py -exec cat {} \; | wc -l;
```
#### Show which extensions are in location
```cmd
find [location] -type f | awk -F. '{print $NF}' | grep -v / | sort | uniq
```
#### Count line of code in files with same extension in location typed in file
```cmd
while read i ; do find [location] -name '*'.$i -exec cat {} \; | wc -l; done < file.txt
```
#### Show life changes in txt file
```cmd
tail -f file.txt
```
