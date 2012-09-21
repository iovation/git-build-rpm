use Module::Build;

my $build = Module::Build->new(
    module_name        => 'git-build-rpm',
    license            => 'perl',
    script_files       => ['bin/git-build-rpm'],
    dist_version_from  => 'bin/git-build-rpm',
    dist_abstract      => 'Build an RPM from a Git repository',
    pm_files           => {},
    configure_requires => { 'Module::Build' => '0.35' },
    build_requires     => { 'Module::Build' => '0.35' },
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
);
$build->create_build_script;
