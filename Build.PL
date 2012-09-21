use Module::Build;

my $build_pkg = eval { require Module::Build::Iovation }
  ? 'Module::Build::Iovation' : 'Module::Build';

my $exec_path = `git --exec-path`;
chomp $exec_path;
my $man_path = `git --man-path`;
chomp $man_path;
unless ($man_path) {
    # --man-dir not implemented; derive it from the exec path.
    my $sep = substr $exec_path, 0, 1;
    ($man_path = $exec_path) =~ s/\blibexec\b.+/share${sep}man${sep}man1/;
}

my $build = $build_pkg->new(
    module_name        => 'git-build-rpm',
    license            => 'perl',
    dist_version_from  => 'bin/git-build-rpm',
    dist_abstract      => 'Build an RPM from a Git repository',
    dist_author        => 'David E. Wheeler <david.wheeler@iovation.com>',
    pm_files           => {},
    configure_requires => { 'Module::Build' => '0.35' },
    build_requires     => { 'Module::Build' => '0.35' },
    install_path       => { script => $exec_path, bindoc => $man_path },
    requires           => {
        perl                => '5.010',
        Getopt::Long        => 0,
        List::Util          => 0,
        IPC::System::Simple => 1.17,
        File::Temp          => 0,
        Path::Class         => 0,
        File::Path          => 0,
        File::Copy          => 0,
        File::Basename      => 0,
        Pod::Usage          => 0,
    },
    requires_rpms => [qw[
        git
        perl(Getopt::Long)
        perl(List::Util)
        perl(IPC::System::Simple)
        perl(File::Temp)
        perl(Path::Class)
        perl(File::Path)
        perl(File::Copy)
        perl(File::Basename)
        perl(Pod::Usage)
    ]],
);
$build->create_build_script;
