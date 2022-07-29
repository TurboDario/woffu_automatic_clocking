# Woffu automatic clocking
 Automating clocking for woffu systems

---

# Configure server (linux)

## Install github

[Guide to install git](https://github.com/git-guides/install-git)

`sudo apt-get install git-all`

## Take project

[How to clone or pull a project](https://linuxhint.com/pull_request_github/)

`git clone https://github.com/TurboDario/woffu_automatic_clocking.git`

## Download and locate webdriver


### Download your geckodriver version in the link below.

[Geckodriver download](https://github.com/mozilla/geckodriver/releases)

### Decompress:

`tar –xvf file.tar.gz`

### Add geckodriver to PATH

`export PATH=$PATH:/path/to/directory/of/executable/downloaded`

If this doesn't work, you can move geckodriver to /usr/local/bin

*Check the correct permissions, maybe you need to add execution permissions in the previous step*

## Configure project for your own use

### Set credentials

Modify user and pass in password.json (Working on a encrypted way to do this)

### Set crontab

[Crontab documentation](https://man7.org/linux/man-pages/man5/crontab.5.html)

[A quick and simple editor for cron schedule expressions.](https://crontab.guru/)

Modify crontab to your calendar and and the correct path to the *clocking_job.sh* file

