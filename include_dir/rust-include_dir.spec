# Generated by rust2rpm 26
%bcond_with check
%global debug_package %{nil}

%global crate include_dir

Name:           rust-include_dir
Version:        0.7.4
Release:        %autorelease
Summary:        Embed the contents of a directory in your binary

License:        MIT
URL:            https://crates.io/crates/include_dir
Source:         %{crates_source}
Source2:        https://raw.githubusercontent.com/Michael-F-Bryan/include_dir/refs/tags/v0.2.1/LICENSE

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Embed the contents of a directory in your binary.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+glob-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glob-devel %{_description}

This package contains library source intended for building other packages which
use the "glob" feature of the "%{crate}" crate.

%files       -n %{name}+glob-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+metadata-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+metadata-devel %{_description}

This package contains library source intended for building other packages which
use the "metadata" feature of the "%{crate}" crate.

%files       -n %{name}+metadata-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
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
