# Microsoft Teams User Info Dump

1. Visit [https://developer.microsoft.com/en-us/graph/graph-explorer](https://developer.microsoft.com/en-us/graph/graph-explorer).
2. In `Authentication`, log in using `Sign in to Graph Explorer`.
3. Select `GET`, `v1.0`, fill in `https://graph.microsoft.com/v1.0/users?$top=999`, and click `Run query`.
4. In `Response preview`, you should find the information in the `"value"` entry.
5. `Ctrl+A`, `Ctrl+C` and save the full response in `page{N}.txt`, and replace `{N}` as the current page number (no leading zeros).
6. Follow the `"@odata.nextLink"` link in `Response preview` and repeat step 4-6 to iteratively retrieve all user information.
7. In the end, you should have `page1.txt`, ..., `page20.txt`, assuming you collected a total of 20 pages of info.
8. Run `python parse.py`, the information should be stored in `output.csv`
