%global tl_name fullblck
%global tl_revision 25434

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	Left-blocking for letter class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fullblck
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Used with the letter documentclass to set the letter in a fullblock
style (everything at the left margin).

