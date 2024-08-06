

export const environment = {
    production: false,
    authDomain: `${process.env["AUTH_DOMAIN"]}`,
    authClientId: `${process.env["AUTH_CLIENT_ID"]}`,
    authAudience: `${process.env["AUTH_AUDIENCE"]}`
}

// production: false,
// authDomain: `${process.env["AUTH_DOMAIN"]}`,
// authClientId: `${process.env["AUTH_CLIENT_ID"]}`,
// authAudience: `${process.env["AUTH_AUDIENCE"]}`


// production: false,
// authDomain: 'dev-qa7eq8kdkth5sh2g.us.auth0.com',
// authClientId: 'aIecwg5MbrpADVvDhsL2aXLtC4Br5JsC',
// authAudience: 'https://budget-todo-auth-backend.com'