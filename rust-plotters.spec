# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate plotters

Name:           rust-plotters
Version:        0.3.7
Release:        %autorelease
Summary:        Rust drawing library focus on data plotting for both WASM and native applications

License:        MIT
URL:            https://crates.io/crates/plotters
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          plotters-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A Rust drawing library focus on data plotting for both WASM and native
applications.}

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

%package     -n %{name}+ab_glyph-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ab_glyph-devel %{_description}

This package contains library source intended for building other packages which
use the "ab_glyph" feature of the "%{crate}" crate.

%files       -n %{name}+ab_glyph-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+all_elements-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all_elements-devel %{_description}

This package contains library source intended for building other packages which
use the "all_elements" feature of the "%{crate}" crate.

%files       -n %{name}+all_elements-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+all_series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all_series-devel %{_description}

This package contains library source intended for building other packages which
use the "all_series" feature of the "%{crate}" crate.

%files       -n %{name}+all_series-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+area_series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+area_series-devel %{_description}

This package contains library source intended for building other packages which
use the "area_series" feature of the "%{crate}" crate.

%files       -n %{name}+area_series-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bitmap_backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bitmap_backend-devel %{_description}

This package contains library source intended for building other packages which
use the "bitmap_backend" feature of the "%{crate}" crate.

%files       -n %{name}+bitmap_backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bitmap_encoder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bitmap_encoder-devel %{_description}

This package contains library source intended for building other packages which
use the "bitmap_encoder" feature of the "%{crate}" crate.

%files       -n %{name}+bitmap_encoder-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bitmap_gif-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bitmap_gif-devel %{_description}

This package contains library source intended for building other packages which
use the "bitmap_gif" feature of the "%{crate}" crate.

%files       -n %{name}+bitmap_gif-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+boxplot-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+boxplot-devel %{_description}

This package contains library source intended for building other packages which
use the "boxplot" feature of the "%{crate}" crate.

%files       -n %{name}+boxplot-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+candlestick-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+candlestick-devel %{_description}

This package contains library source intended for building other packages which
use the "candlestick" feature of the "%{crate}" crate.

%files       -n %{name}+candlestick-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+colormaps-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+colormaps-devel %{_description}

This package contains library source intended for building other packages which
use the "colormaps" feature of the "%{crate}" crate.

%files       -n %{name}+colormaps-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+datetime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+datetime-devel %{_description}

This package contains library source intended for building other packages which
use the "datetime" feature of the "%{crate}" crate.

%files       -n %{name}+datetime-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+deprecated_items-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deprecated_items-devel %{_description}

This package contains library source intended for building other packages which
use the "deprecated_items" feature of the "%{crate}" crate.

%files       -n %{name}+deprecated_items-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+errorbar-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+errorbar-devel %{_description}

This package contains library source intended for building other packages which
use the "errorbar" feature of the "%{crate}" crate.

%files       -n %{name}+errorbar-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+evcxr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+evcxr-devel %{_description}

This package contains library source intended for building other packages which
use the "evcxr" feature of the "%{crate}" crate.

%files       -n %{name}+evcxr-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+evcxr_bitmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+evcxr_bitmap-devel %{_description}

This package contains library source intended for building other packages which
use the "evcxr_bitmap" feature of the "%{crate}" crate.

%files       -n %{name}+evcxr_bitmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+font-kit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+font-kit-devel %{_description}

This package contains library source intended for building other packages which
use the "font-kit" feature of the "%{crate}" crate.

%files       -n %{name}+font-kit-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fontconfig-dlopen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fontconfig-dlopen-devel %{_description}

This package contains library source intended for building other packages which
use the "fontconfig-dlopen" feature of the "%{crate}" crate.

%files       -n %{name}+fontconfig-dlopen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+full_palette-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full_palette-devel %{_description}

This package contains library source intended for building other packages which
use the "full_palette" feature of the "%{crate}" crate.

%files       -n %{name}+full_palette-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+histogram-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+histogram-devel %{_description}

This package contains library source intended for building other packages which
use the "histogram" feature of the "%{crate}" crate.

%files       -n %{name}+histogram-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+image-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+image-devel %{_description}

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%files       -n %{name}+image-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+line_series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+line_series-devel %{_description}

This package contains library source intended for building other packages which
use the "line_series" feature of the "%{crate}" crate.

%files       -n %{name}+line_series-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+once_cell-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+once_cell-devel %{_description}

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%files       -n %{name}+once_cell-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pathfinder_geometry-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pathfinder_geometry-devel %{_description}

This package contains library source intended for building other packages which
use the "pathfinder_geometry" feature of the "%{crate}" crate.

%files       -n %{name}+pathfinder_geometry-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+plotters-bitmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+plotters-bitmap-devel %{_description}

This package contains library source intended for building other packages which
use the "plotters-bitmap" feature of the "%{crate}" crate.

%files       -n %{name}+plotters-bitmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+plotters-svg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+plotters-svg-devel %{_description}

This package contains library source intended for building other packages which
use the "plotters-svg" feature of the "%{crate}" crate.

%files       -n %{name}+plotters-svg-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+point_series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+point_series-devel %{_description}

This package contains library source intended for building other packages which
use the "point_series" feature of the "%{crate}" crate.

%files       -n %{name}+point_series-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+surface_series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+surface_series-devel %{_description}

This package contains library source intended for building other packages which
use the "surface_series" feature of the "%{crate}" crate.

%files       -n %{name}+surface_series-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+svg_backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+svg_backend-devel %{_description}

This package contains library source intended for building other packages which
use the "svg_backend" feature of the "%{crate}" crate.

%files       -n %{name}+svg_backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ttf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ttf-devel %{_description}

This package contains library source intended for building other packages which
use the "ttf" feature of the "%{crate}" crate.

%files       -n %{name}+ttf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ttf-parser-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ttf-parser-devel %{_description}

This package contains library source intended for building other packages which
use the "ttf-parser" feature of the "%{crate}" crate.

%files       -n %{name}+ttf-parser-devel
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
