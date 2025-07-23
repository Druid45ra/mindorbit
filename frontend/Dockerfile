# Etapa 1: Build stage
FROM node:20-alpine AS builder

# Setează directorul de lucru
WORKDIR /app

# Copiază fișierele de configurare și instalare
COPY package.json package-lock.json ./

# Instalează dependențele
RUN npm ci

# Copiază restul codului
COPY . .

# Construiește aplicația pentru producție
RUN npm run build

# Etapa 2: Production stage
FROM nginx:alpine

# Copiază fișierele build în NGINX
COPY --from=builder /app/dist /usr/share/nginx/html

# Copiază configurarea custom NGINX (opțional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expune portul implicit NGINX
EXPOSE 80

# Rulează NGINX
CMD ["nginx", "-g", "daemon off;"]
