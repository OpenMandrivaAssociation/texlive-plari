%global tl_name plari
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typesetting stageplay scripts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/plari
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plari.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plari.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plari.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Plari (the name comes from the Finnish usage for the working copy of a
play) is a report-alike class, without section headings, and with
paragraphs vertically separated rather than indented.

