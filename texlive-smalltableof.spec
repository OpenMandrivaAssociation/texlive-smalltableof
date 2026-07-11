%global tl_name smalltableof
%global tl_revision 20333

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Create listoffigures etc. in a single chapter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/smalltableof
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smalltableof.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smalltableof.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows you to create a list of figures and list of tables in
a chapter named 'List' that contains separate sections for each list of
figures, tables, etc.

