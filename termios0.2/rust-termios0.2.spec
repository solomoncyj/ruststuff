# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate termios

Name:           rust-termios0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Safe bindings for the termios library

License:        MIT
URL:            https://crates.io/crates/termios
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Safe bindings for the termios library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
# remove executable bit
chmod -x %{buildroot}/usr/share/cargo/registry/termios-%{version}/src/os/freebsd.rs
chmod -x %{buildroot}/usr/share/cargo/registry/termios-%{version}/src/os/openbsd.rs

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
