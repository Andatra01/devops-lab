FROM node:20-alpine
WORKDIR /app
COPY package*.json .
RUN npm install express
COPY . .
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
EXPOSE 3002

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD wget -q --spider http://localhost:3002/heath || exit

CMD ["node", "app.js"]