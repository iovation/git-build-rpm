git-build-rpm
=============

Build RPMs from Git repositories.

Description
-----------

This project makes it easy to create RPMs from Git projects. Simply create an
[RPM Spec file](https://fedoraproject.org/wiki/How_to_create_an_RPM_package)
with the same name as your Git repository in a directory named `dist` at the
root of your project. This project is a good example: See
[`dist/git-build-rpm.spec`](dist/git-build-rpm.spec) for an example. Then just
run `git-build-rpm` to build your RPM:

    git build-rpm

`git-build-rpm` will archive the current branch of your repository, as well
as any submodules, and then call `rpmbuild` to build from the archive based
on the spec file. Once the RPM has been built, it will be dropped in the root
directory of your project, from where you can copy it to your RPM repository
of choice.

Installation
------------

Install dependencies via YUM:

    sudo yum install git git-archive-all rpm-build \
                     'perl(Module::Build)' \
                     'perl(IPC::System::Simple)' \
                     'perl(Path::Class)'



Install dependencies via DNF and pip:

    sudo dnf install git rpm-build perl-rpm-build-perl perl-IPC-System-Simple \
    			perl-Path-Class perl-Test-Pod perl-Module-Build

    sudo pip install --upgrade pip
    sudo pip install git-archive-all

Build and install from Source:

    perl Build.PL
    ./Build
    sudo ./Build install

Build and install an RPM:

    ./bin/git-build-rpm
    rpm -Uvh git-build-rpm*.rpm

Options
-------

* `--spec-file`: Path to RPM spec file.
* `--archive-ext`: Extension used for creating archive
* `--git`: Path to git program.
* `--git-branch`: Git branch to build from.
* `-p` `--package-name`: Name of the project, used to archive the repo.
* `-v` `--package-version`: Version of the package, used in the RPM release name.
* `--dist`: Name of distribution, used in RPM release name.
* `-D` `--define`:  Define macro=value.
* `--rpm-dir`: Path to directory for building the RPM.
* `--quiet`: Print as little as possible.
* `-V` `--version`: Print the version number and exit.
* `-H` `--help`: Print a usage statement and exit.
* `-M` `--man`: Print the complete documentation and exit.

How it Works
------------

Here's what `git-build-rpm` does when you run it:

*   Determines the current branch name via the `--git-branch` option,
    `$GIT_BRANCH` environment variable, or by parsing the output of
    `branch -a --contains HEAD`.

*   Determines the package name via the `--package-name` option or the
    output of `git remote -v`, preferring origin, and parsing it from
    the last part of the remote URL, ending in `.git`.

*   Determines the directory in which to build the RPM, using either the
    `--rpm-dir` option or a temporary directory that will be deleted on exit.

*   Determines the path to the RPM spec file, via the `--spec-file` option
    or by looking for a file named `./dist/$package_name.spec`.

*   Unless specified via the `--pakcage-version` option, Extracts the version
    from the spec file. It tries using `rpmspec`, but if it's not available,
    it parses the version from the spec file directly. If that extracted
    version appears to be a macro, it will be run through `rpm -E` for
    evaluation.

*   Copies the spec file to the RPM build SPECS directory.

*   Archives the specified branch of the repository, as well as any
    submodules, into the RPM build SOURCES directory using supplied --archive-ext
    to determine archive type. Defaults to tar.gz.

*   Determines the RPM `dist` value via the `--dist` option, defaulting to the
    current epoch time and OS version. If the current branch is not "master",
    the branch name is also included in the `dist` value (with any invalid
    characters replaced with underscores). That is, the value is something
    like `1434755064.el7` when building master, and
    `1434755064.$branch_name_.el7` when building from any other branch.

*   Builds the RPM, setting `dist` and any other parameters passed via the
    `--define` option.

*   Moves all resulting RPMs to the current directory.

Copyright & License
-------------------
Copyright 2012-1015 [iovation, Inc.](http://iovation.com/) Some Rights
Reserved.

This program is free software; you can redistribute it and/or modify it under
the same terms as Perl itself.

Author
------
* [David E. Wheeler](mailto:david.wheeler@iovation.com)
