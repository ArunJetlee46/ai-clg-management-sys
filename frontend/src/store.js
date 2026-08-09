import { create } from 'zustand'

export const useAuthStore = create((set) => ({
  token: '',
  setToken: (token) => set({ token }),
}))
