# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate portable-pty

Name:           rust-portable-pty
Version:        0.9.0
Release:        %autorelease
Summary:        Cross platform pty interface

License:        MIT
URL:            https://crates.io/crates/portable-pty
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          portable-pty-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Cross platform pty interface.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_derive-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%files       -n %{name}+serde_derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_support-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_support" feature of the "%{crate}" crate.

%files       -n %{name}+serde_support-devel
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
