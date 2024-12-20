# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate serial-unix

Name:           rust-serial-unix
Version:        0.4.0
Release:        %autorelease
Summary:        Serial port implementation for Unix

License:        MIT
URL:            https://crates.io/crates/serial-unix
Source:         %{crates_source}
Source2:        https://raw.githubusercontent.com/tree-sitter/tree-sitter/refs/heads/master/LICENSE
# Manually created patch for downstream crate metadata changes
Patch:          serial-unix-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Serial port implementation for Unix.}

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
cp -p %SOURCE2 .
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
