-- Lua script takes implements Keycloak reverse proxy
local opts = {
    redirect_uri_path = "/redirect_uri",
    accept_none_alg = true,
    discovery = "https://${KEYCLOAK_SERVER}/auth/realms/${KEYCLOAK_REALM}/.well-known/openid-configuration",
    client_id = "${KEYCLOAK_CLIENT_ID}",
    client_secret = "${KEYCLOAK_CLIENT_SECRET}",
    redirect_uri_scheme = "http",
    logout_path = "/logout",
    redirect_after_logout_uri = "http://${KEYCLOAK_SERVER}/auth/realms/${KEYCLOAK_REALM}/protocol/openid-connect/logout?redirect_uri=http://localhost",
    redirect_after_logout_with_id_token_hint = false,
    session_contents = {id_token=true},
}

-- call introspect for OAuth 2.0 Bearer Access Token validation
local res, err = require("resty.openidc").authenticate(opts)
if err then
    ngx.status = 403
    ngx.say(err)
    ngx.exit(ngx.HTTP_FORBIDDEN)
end