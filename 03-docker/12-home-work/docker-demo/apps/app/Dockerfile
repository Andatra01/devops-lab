FROM node:16-alpine as node
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
WORKDIR /app/apps/app

RUN npm install @types/minimatch --save-dev

ARG env=prod
RUN CI=false SKIP_PREFLIGHT_CHECK=true TSC_COMPILE_ON_ERROR=true PUBLIC_URL=http://127.0.0.1:3001 npm run build

FROM nginx:1.13
COPY --from=node /app/apps/app/build /usr/share/nginx/html
COPY ./apps/app/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80