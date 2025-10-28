{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = with pkgs; [
    python313
    python313Packages.pytest
    python313Packages.debugpy
    python313Packages.flake8
  ];

  shellHook = ''
   code .
  '';
}
