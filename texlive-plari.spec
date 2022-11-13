Name:		texlive-plari
Version:	15878
Release:	1
Summary:	Typesetting stageplay scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/plari
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plari.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plari.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plari.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Plari (the name comes from the Finnish usage for the working
copy of a play) is a report-alike class, without section
headings, and with paragraphs vertically separated rather than
indented.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/plari/plari.cls
%doc %{_texmfdistdir}/doc/latex/plari/COPYING
%doc %{_texmfdistdir}/doc/latex/plari/README
%doc %{_texmfdistdir}/doc/latex/plari/plari.pdf
#- source
%doc %{_texmfdistdir}/source/latex/plari/Makefile
%doc %{_texmfdistdir}/source/latex/plari/plari.dtx
%doc %{_texmfdistdir}/source/latex/plari/plari.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
