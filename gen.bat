call rmdir /Q "c:\sources\omsa"
call openapi bundle OMSA.yaml -o bundled.yaml
call npx @openapitools/openapi-generator-cli validate -i bundled.yaml
call npx @openapitools/openapi-generator-cli generate -g kotlin -o c:/sources/omsa/ -i .\OMSA.yaml