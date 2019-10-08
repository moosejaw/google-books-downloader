# Google Books Downloader
This tool downloads the contents of a Google books preview to a collection of `.png` files. These images can then be converted into `.pdf` files using tools such as [this one](https://png2pdf.com/). Use this responsibly!

It runs in Python 3.x.

## Important Note
On MacOS you may need to install SSL certificates for Python 3.x by running:
```bash
/Applications/Python\ 3.7/Install\ Certificates.command
```

## Running the downloader
To run this downloader you need to acquire a `.har` file containing all of the GET requests your browser made for the image files.

To do this, open your browser and open the Network tab of your developer tools, or whichever tab allows you to view outgoing HTTP requests.

Once the request analyser is open, navigate to the Google books preview page of the book you wish to capture. Then, scroll through every page you need. For example, if I needed pages 195-205 of a preview which contains pages 170-220, I would modify the URL to point to pg. 195. The easiest way to do this is to search for a string of text in the page you want to start with, and then click the search result pointing to that page. You can then open the request analyser in a new tab and navigate to the URL.

Once you have a starting page set up and the requests are being tracked by your browser, scroll to the final page you need.

Next, save the captured requests as a `.har` file. Firefox can do this by right clicking on any request, and selecting 'Save All as HAR'.

Then, select a request which returned one of the images you need (i.e., a request in the list that returned a `.png` file) and view the request headers. Copy/paste the **value** of your Cookie and User Agent headers into a text utility such as Notepad, vim, etc.

Then, copy your Cookie and User Agent values into the `HEADER` global variable in `downloader.py`.

You can also modify the other global variables to adjust the input file or the output. For example, you should repoint the `HAR\_FILE` variable to the `.har` file you downloaded. You may also need to manually create the directory to which you save the image files, as specified in `OUTPUT\_FOLDER`.

Now, run the script from your command window. You should notice that the output folder is populated with a new image every two seconds.

## Image Not Available
If the image files mostly contain a generic 'Image Not Available' picture, you may need to double check your Cookie and User Agent values are correct.
