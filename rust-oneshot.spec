# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate oneshot

Name:           rust-oneshot
Version:        0.1.8
Release:        %autorelease
Summary:        Spsc channel with

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/oneshot
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          oneshot-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Oneshot spsc channel with (potentially) lock-free non-blocking send, and
a receiver supporting both thread blocking receive operations as well as
Future based async polling.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
# FIXME: no license files detected
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-devel %{_description}

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%files       -n %{name}+async-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
