Name: sdl2-examples
Version: 0.1
Release: alt1
Packager: NICourced
Summary: examples collection progs
License: GPLv2
Group: Game
URL: https://github.com/xyproto/sdl2-examples
Source0: %{name}-%{version}.tar.gz
BuildRequires: gcc gcc-c++ libSDL2-devel libSDL2_mixer-devel libSDL2_net-devel libSDL2_image-devel libSDL2_ttf-devel golang nasm pkg-config mono-core dmd freebasic dotnet go java kotlin clang fpc python3-module-sdl2 zig
BuildRequires: sbcl lua5.3 lua5.3-devel lua5.3-luarocks
BuildRequires: desktop-file-utils
Requires: icon-theme-hicolor

%description
EXAMPLES

%prep
%setup -q

%build

for dir in *; do
    [ -d "$dir" ] || continue
    cd "$dir"
    if [ -f Makefile ]; then
        %make_build || echo "make failed in $dir"
    elif [ -f CmakeLists.txt ]; then
        mkdir -p build
        cd build
        cmake .. -DCMAKE_BUILD_TYPE=Release || echo "cmake configure failed in $dir"
        make || echo "cmake build failed in $dir"
        cd ..
    fi
    cd ..
done

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/img

cp -a img/* %{buildroot}%{_datadir}/img/
i=1
for dir in *; do
    [ -d "$dir" ] || continue
    exe=$(find "$dir" -maxdepth 1 -type f -executable | head -n1)
    [ -z "$exe" ] && exe=$(find "$dir"/build -type f -executable | head -n1)
    [ -z "$exe" ] && continue
    name=%{name}-$dir
    install -m 0755 "$exe" %{buildroot}%{_bindir}/$name
    echo -e "[Desktop Entry]\nName=SDL2Example ${i}\nComment=Example ${i} from SDL2-examples\nExec=${name}\nPath=/usr/share/applications\nIcon=application-games\nTerminal=false\nType=Application\nCategories=Game;\n" > %{buildroot}%{_datadir}/applications/$name.desktop
    let i++
done



%files

%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/img/*

%changelog
* Wed Jun 18 2025 NICourced <nicourced@mail.ru> 0.1-alt1
- Spec for some tests

