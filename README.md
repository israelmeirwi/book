This is a textbook that we are writing on informal homotopy type theory.
It is part of the [Univalent foundations of mathematics](http://www.math.ias.edu/sp/univalent)
project which took place at the Institute for Advanced Study in 2012/13.

## License

This work is licensed under the
[Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

### Prerequisites and compilation

To compile the book you need a fairly new version of LaTeX.
[Texlive](http://www.tug.org/texlive/) 2012 is confirmed to work. You might need
to install some packages, see `main.tex` for packages that are used by the book.

[BasicTeX](http://www.tug.org/mactex/morepackages.html), which is a minimalistic
version of MacTeX is confirmed to work once the following packages have been
installed: `tlmgr`, `install`, `braket`, `comment`, `courier`, `enumitem`,
`helvetic`, `mathpazo`, `nextpage`, `ntheorem`, `palatino`, `rsfs`, `stmaryrd`,
`symbol`, `titlesec`, `wallpaper`, `wasy`, `wasysym`, `xstring`, `zapfding`.

You also need the `make` utility. The book is a fairly complex piece of LaTeX
code. Also, the file `version.tex` is generated on the fly, so you will need the
`make` utlity with which you can compile the main files, as follows:

* `make hott-online.pdf` -- the book appropriate for online reading, with colors and green links
* `make hott-ebook.pdf` -- the book with small margins, suitable for ebook readers
* `make hott-letter.pdf hott-cover.pdf` -- the book in black & white, letter paper format,
   for printing at home, as well as a color cover (just two pages)
* `make hott-a4.pdf hott-a4.pdf` -- the book in black & white, A4 paper format,
   for printing at home, as well as a color cover (just two pages)
* `make hott-ustrade.pdf cover-lulu.pdf` -- the book in US Trade format, without cover,
   used for the bound copy available at http://lulu.com/
* `make exercise_solutions.pdf` -- compile (some) solutions to exercises

If you do not have `make` (for example, because you are on MacOS and you did not
install the XCode command-line utilities), you can still fake it as follows.
Create the file `version.txt` and put in it (where "Joe Hacker" should be
replaced with your name):

    \newcommand{\OPTversion}{Joe-Hacker-version}

Then use whatever tools you normally do to compile LaTeX. The main LaTeX files are called 
`hott-XXX.tex`. But you really should have `make`, you know.

Once `make` is run so that `version.txt` gets generated, you need not run
`make` again. You can just perform the usual LaTeX cycle from your favorite editor.

## Smoking Cessation App Example

A minimal Flask application to help track smoking cessation progress and run friendly competitions. Install dependencies from `smoking_app/requirements.txt` and run `python smoking_app/app.py`.

### Getting a shareable link

To let other people try the demo without running it locally, you can deploy it to a hosted platform such as [Render](https://render.com/):

1. Commit the repository to your own GitHub account.
2. Visit Render and choose **New ➜ Blueprint**. Point it at your GitHub repository.
3. Render will detect the provided `render.yaml` file and create a web service that installs dependencies with `pip install -r smoking_app/requirements.txt` and serves the Flask app through Gunicorn.
4. Once the build finishes, Render exposes a public HTTPS URL you can share. The blueprint also provisions a persistent disk and sets `DATABASE_URL` and `SECRET_KEY` automatically so that the SQLite database survives restarts.

If you prefer another host (Heroku, Railway, etc.), configure it to run `gunicorn smoking_app.app:create_app()` after installing the dependencies, and set the `DATABASE_URL` environment variable to the database connection string you want to use.
