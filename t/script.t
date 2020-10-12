#!/usr/bin/perl -w

use strict;
use Test::More tests => 1;
use File::Spec::Functions;

# Silence "Syntax OK".
close STDERR;
my $ret = system $^X, '-cw', catfile(curdir, 'bin', 'git-build-rpm');
ok !$ret;
