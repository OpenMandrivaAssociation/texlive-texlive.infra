Name:		texlive-texlive.infra
Version:	63645
Release:	2
Summary:	basic TeX Live infrastructure
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texlive.infra
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive.infra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive.infra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains the files needed to get tlmgr running:
perl modules, xz binaries, plus (sometimes) tar, wget, lz4, and
various other support files. This package also represents the
tlcritical recovery scripts. The standalone installer is close,
but not the same; it's defined in 00texlive.installer.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/release-texlive.txt
%{_texmfdistdir}/LICENSE.TL
%{_texmfdistdir}/LICENSE.CTAN
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/web2c
%{_texmfdistdir}/texmf-dist/web2c/updmap-hdr.cfg
%{_texmfdistdir}/texmf-dist/web2c/fmtutil-hdr.cnf
%{_texmfdistdir}/texmf-dist/scripts
%{_texmfdistdir}/texmf-dist/scripts/texlive
%{_texmfdistdir}/texmf-dist/scripts/texlive/uninstq.vbs
%{_texmfdistdir}/texmf-dist/scripts/texlive/uninstall-win32.pl
%{_texmfdistdir}/texmf-dist/scripts/texlive/tlmgrgui.pl
%{_texmfdistdir}/texmf-dist/scripts/texlive/tlmgr.pl
%{_texmfdistdir}/texmf-dist/scripts/texlive/tl-errmess.vbs
%{_texmfdistdir}/texmf-dist/scripts/texlive/mktexlsr
%{_texmfdistdir}/texmf-dist/scripts/texlive/NEWS
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/tlmgr.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/tlmgr.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/mktexlsr.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/mktexlsr.1
%{_texmfdistdir}/readme-txt.dir
%{_texmfdistdir}/readme-txt.dir/README.ZH-CN
%{_texmfdistdir}/readme-txt.dir/README.VI
%{_texmfdistdir}/readme-txt.dir/README.SR
%{_texmfdistdir}/readme-txt.dir/README.SK
%{_texmfdistdir}/readme-txt.dir/README.RU-koi8
%{_texmfdistdir}/readme-txt.dir/README.RU-cp1251
%{_texmfdistdir}/readme-txt.dir/README.RU
%{_texmfdistdir}/readme-txt.dir/README.PT-BR
%{_texmfdistdir}/readme-txt.dir/README.PL
%{_texmfdistdir}/readme-txt.dir/README.JA
%{_texmfdistdir}/readme-txt.dir/README.IT
%{_texmfdistdir}/readme-txt.dir/README.FR
%{_texmfdistdir}/readme-txt.dir/README.ES
%{_texmfdistdir}/readme-txt.dir/README.EN
%{_texmfdistdir}/readme-txt.dir/README.DE
%{_texmfdistdir}/readme-txt.dir/README.CS
%{_texmfdistdir}/readme-html.dir
%{_texmfdistdir}/readme-html.dir/readme.zh-cn.html
%{_texmfdistdir}/readme-html.dir/readme.vi.html
%{_texmfdistdir}/readme-html.dir/readme.sr.html
%{_texmfdistdir}/readme-html.dir/readme.sk.html
%{_texmfdistdir}/readme-html.dir/readme.ru.html
%{_texmfdistdir}/readme-html.dir/readme.pt-br.html
%{_texmfdistdir}/readme-html.dir/readme.pl.html
%{_texmfdistdir}/readme-html.dir/readme.ja.html
%{_texmfdistdir}/readme-html.dir/readme.it.html
%{_texmfdistdir}/readme-html.dir/readme.fr.html
%{_texmfdistdir}/readme-html.dir/readme.es.html
%{_texmfdistdir}/readme-html.dir/readme.en.html
%{_texmfdistdir}/readme-html.dir/readme.de.html
%{_texmfdistdir}/readme-html.dir/readme.cs.html
%{_texmfdistdir}/index.html
%{_texmfdistdir}/README.usergroups
%{_texmfdistdir}/README

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
